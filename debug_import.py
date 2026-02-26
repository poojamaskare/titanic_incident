import traceback
try:
    import backend.app.routes.chat as m
    print('module OK')
except Exception:
    traceback.print_exc()
