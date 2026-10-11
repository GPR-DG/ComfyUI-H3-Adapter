from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, STORE
WEB_DIRECTORY = './web'

try:
    from server import PromptServer
except ModuleNotFoundError as error:
    if error.name != 'server':
        raise
else:
    from .h3_adapter.routes import register_routes
    register_routes(PromptServer.instance.routes, STORE)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
