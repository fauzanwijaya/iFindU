import requests
import json
import time
import sys
from colorama import Fore, Style, init

class InstagramBot:
    """
    Bot Instagram untuk menentukan pengguna yang tidak mem-follow-back.
    """

    def __init__(self, session_cookie):
        """
        Inisialisasi bot dengan session cookie.
        """
        self.session = requests.Session()
        self.session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        })
        self.session.cookies.update({'sessionid': session_cookie})
        self.base_url = 'https://www.instagram.com'
        init(autoreset=True)

    def _cetak_progress(self, pesan):
        """
        Mencetak pesan progress pada baris yang sama.
        """
        sys.stdout.write('\r' + ' ' * 100)
        sys.stdout.write('\r')
        sys.stdout.flush()
        print(Fore.CYAN + pesan, end='', flush=True)

    def _ambil_data_follow(self, user_id, query_hash, nama_edge, end_cursor=''):
        """
        Mengambil data followers atau following dari Instagram.
        """
        self._cetak_progress(f"Mengambil data untuk {nama_edge}...")
        url = f'{self.base_url}/graphql/query/'
        variables = {
            'id': user_id,
            'include_reel': True,
            'fetch_mutual': False,
            'first': 50,
            'after': end_cursor
        }
        params = {
            'query_hash': query_hash,
            'variables': json.dumps(variables)
        }
        response = self.session.get(url, params=params)
        time.sleep(2)
        data = response.json()['data']['user'][nama_edge]
        return data['edges'], data['page_info']

    def _ambil_data_lengkap_follow(self, user_id, query_hash, nama_edge):
        """
        Mengumpulkan data lengkap followers atau following.
        """
        self._cetak_progress(f"Mengumpulkan daftar lengkap untuk {nama_edge}...")
        pengguna, info_halaman = self._ambil_data_follow(user_id, query_hash, nama_edge)
        while info_halaman['has_next_page']:
            pengguna_tambahan, info_halaman = self._ambil_data_follow(user_id, query_hash, nama_edge, info_halaman['end_cursor'])
            pengguna.extend(pengguna_tambahan)
            self._cetak_progress(f"Jumlah {nama_edge} terkumpul: {len(pengguna)}")
            time.sleep(2)
        return [user['node'] for user in pengguna]

    def temukan_non_followers(self, user_id):
        """
        Menentukan pengguna yang tidak mem-follow-back.
        """
        self._cetak_progress("Memulai proses untuk menemukan non-followers...")
        followers = self._ambil_data_lengkap_follow(user_id, 'c76146de99bb02f6415203be841dd25a', 'edge_followed_by')
        following = self._ambil_data_lengkap_follow(user_id, 'd04b0a864b4b54837c0d870b0e77e076', 'edge_follow')

        username_followers = {user['username'] for user in followers}
        non_followers = [user for user in following if user['username'] not in username_followers]

        return non_followers

# Penggunaan
session_cookie = 'Ganti dengan nilai cookie sessionid Anda'
user_id = 'Ganti dengan nilai user_id Anda'
bot = InstagramBot(session_cookie)
non_followers = bot.temukan_non_followers(user_id)

print(Style.RESET_ALL)
print("\nNon-followers ditemukan:")
for user in non_followers:
    print(user['username'])
