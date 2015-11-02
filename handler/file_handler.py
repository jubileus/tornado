# coding=UTF-8

import os
from handler.base_handler import BaseHandler

__author__ = 'jubileus'

file_path = '/home/jubileus/'


class FileHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('file.html')


class UploadFileHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        # upload_path = os.path.join(os.path.dirname(__file__), 'files')
        upload_path = os.path.join(file_path, 'files')
        # 提取表单中‘name’为‘file’的文件元数据
        file_metas = self.request.files['file']
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            # 有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
            self.write('''
                <html>
                    <head><title>Upload File</title></head>
                    <body>
                        <h3>上传成功</h3>
                        <a href="/file">返回</a>
                    </body>
                </html>
                       ''')


class DownloadFileHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        filename = self.get_argument('filename')
        if filename:
            try:
                print('i download file handler : ', filename)
                download_path = os.path.join(file_path, 'files', filename)
                # 读取的模式需要根据实际情况进行修改
                exist = False
                with open(download_path, 'rb') as f:
                    # Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
                    self.set_header('Content-Type', 'application/octet-stream')
                    self.set_header('Content-Disposition', 'attachment; filename=' + filename)
                    exist = True
                    while True:
                        data = f.read(1024)
                        if not data:
                            break
                        self.write(data)
                # 记得有finish哦
                if exist:
                    self.finish()
                else:
                    self.write('''
                    <html>
                        <head><title>Download File</title></head>
                        <body>
                            <h3>文件不存在</h3>
                            <a href="/file">返回</a>
                        </body>
                    </html>
                           ''')
            except Exception:
                self.write('''
                    <html>
                        <head><title>Download File</title></head>
                        <body>
                            <h3>文件不存在</h3>
                            <a href="/file">返回</a>
                        </body>
                    </html>
                           ''')
        else:
            self.write('''
                <html>
                    <head><title>Download File</title></head>
                    <body>
                        <h3>文件不存在</h3>
                        <a href="/file">返回</a>
                    </body>
                </html>
                       ''')
