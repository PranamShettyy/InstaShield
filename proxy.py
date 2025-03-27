from mitmproxy import http
import sys 
import filter_img

class ChangeHTTPCode:

    filt = "stp=dst-jpg_e"

    def response(self, flow: http.HTTPFlow) -> None:
        if (self.filt in flow.request.pretty_url):
            if flow.response.headers[b'content-type']=='image/jpeg':
                with open('a.jpeg','wb') as f:
                    f.write(flow.response.content)
                #sys.exit(0)

            if filter_img.is_explict('a.jpeg'):
                flow.response.content=b'None'

addons = [ChangeHTTPCode()] 