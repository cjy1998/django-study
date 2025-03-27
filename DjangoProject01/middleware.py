import json

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ResponseMsgMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        # 在视图函数处理请求之后，响应返回客户端之前被调用
        # 检查响应是否是 JsonResponse 或者其内容类型是 JSON
        if isinstance(response, JsonResponse) or (
                response.has_header('Content-Type') and 'application/json' in response['Content-Type']):
            try:
                # 尝试解析响应内容为 JSON
                if hasattr(response, 'content'):
                    content = json.loads(response.content.decode('utf-8'))
                else:
                    content = {}  # 如果没有 content 属性，默认为空字典

                # 添加一层数据封装
                wrapped_data = {
                    'status': 'success',
                    'data': content,
                    'message': '请求成功',  # 可选
                }

                # 创建新的 JsonResponse
                response = JsonResponse(wrapped_data, status=response.status_code,
                                        json_dumps_params=getattr(response, 'json_dumps_params', None))
            except json.JSONDecodeError:
                # 如果响应内容不是有效的 JSON，则不进行修改
                pass
            except Exception as e:
                # 处理其他可能发生的异常
                print(f"处理 JSON 响应时发生错误: {e}")
                pass
        return response
