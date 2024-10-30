from litestar import get

@get("/health")
async def health_check():
    return {"status": "ok"}
