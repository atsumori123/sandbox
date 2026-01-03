import ftplib
import os

def ftp_upload(hostname, username, password, src_path):
	# ファイルサイズの取得
	file_size = os.path.getsize(src_path)
	# 書き込み総サイズ
	total_write_size = 0

	# FTP接続/アップロード
	with ftplib.FTP() as ftp:
		try:	
			ftp.connect(host=hostname, port=21, timeout=50)
			# パッシブモード設定
			ftp.set_pasv("true")
			# FTPサーバログイン
			ftp.login(username, password)

			for index in range(5):
				with open(src_path, 'rb') as fp:
					dst_path = './temp/test_' + str(index+1).zfill(4) + '.png'
					ftp.storbinary('STOR {}'.format(dst_path), fp)

				total_write_size += file_size
				print(str(index+1).zfill(4) + ': ' + format(int(total_write_size/1024/1024), ',') + ' MByte')
		
		except ftplib.all_errors as e:
			print('FTP error = %s' %e)


# 接続先サーバーのホスト名
hostname = "192.168.10.180" 
# アップロードするファイルパス
src_path = "./img_001.png" 
# サーバーのユーザー名
username = "u20" 
# サーバーのログインパスワード
password = "u20lts" 

ftp_upload(hostname, username, password, src_path)

