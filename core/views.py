from django.views import View

class BaseView(View):
  CONTENT_TYPE:str = 'Content-Type'
  APPLICATION_JSON:str = 'application/json'
  APPLICATION_WWW_FORM_URLENCODED:str = 'application/x-www-form-urlencoded'
  XML_HTTP_REQUEST:str = 'XMLHttpRequest'
  
  def extract_content_type(self) -> str:
    return self.request.headers.get(self.CONTENT_TYPE)
  
  def request_is_ajax(self) -> bool:
    content_type = self.extract_content_type(self.request)
    return content_type in {self.APPLICATION_JSON, self.XML_HTTP_REQUEST}