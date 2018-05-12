import os
from http.server import SimpleHTTPRequestHandler, HTTPServer


class RequestHandler(SimpleHTTPRequestHandler):
    '''处理请求并返回页面'''

    page = '''
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''
    Cases = [case_no_file(),case_existing_file(),case_always_fail()]


    def do_GET(self):
        try:
            full_path = os.getcwd() + self.path
            for case in self.Cases:
                if case.test(self):
                    case.act(self)


#     page = self.create_page()
#     self.send_content(page)
#
# def create_page(self):
#     values = {'date_time' : self.date_time_string(),
#               'client_host' : self.client_address[0],
#               'client_port' : self.client_address[1],
#               'command' : self.command,
#               'path' : self.path
#               }
#     page = self.page.format(**values)
#     return page


#         try:
#             full_path = os.getcwd() + self.path
#             if not os.path.exists(full_path):
#                 raise ServerException('"{0}" not found'.format(self.path))
#             elif os.path.isfile(full_path):
#                 self.handle_file(full_path)
#             else:
#                 raise ServerException('Unknow object "{0}"'.format(self.path))
#
#         except Exception as msg:
#             self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path,'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = '"{0}" cannot be read: {1}'.format(self.path,msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path = self.path,msg = msg)
        self.send_content(content,404)

    def send_content(self,content,status = 200):
        self.send_response(status)
        self.send_header("Content-type","text-html")
        self.send_header("Context-Length",str(len(content)))
        self.end_headers()
        self.wfile.write(bytes(content))

    Error_Page = '''
    <html>
    <body>
    <h1>Error accessing {path}</h1>
    <p>{msg}</p>
    </body>
    </html>
    '''

class ServerException(Exception):
    '''服务器内部错误'''
    pass

class case_no_file(object):
    def test(self,handler):
        return not os.path.exists(handler.full_path)

    def act(self,handler):
        raise ServerException('"{0}" not found'.format(handler.path))

class case_existing_file(object):
    def test(self,handler):
        return os.path.isfile(handler.full_path)

    def act(self,handler):
        handler.handle_file(handler.full_path)

class case_always_fail(object):
    '''所有情况都不符合时的默认处理类'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))




if __name__ == "__main__":
    serverAddress = ('',8080)
    server = HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

