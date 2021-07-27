import hashlib
from urllib.parse import urlparse

from fastapi import APIRouter, HTTPException, Request

from ..utils.store_connector import StoreConnector
from ..models.urls import Url
from starlette.responses import RedirectResponse

router = APIRouter()
store = StoreConnector().store


def _get_base_url(endpoint_url: str) -> str:
    """
    Extract base url from any endpoint URL.
    :param endpoint_url: Endpoint URL from which the base URL is to be extracted.
    :return: Base URL
    """
    return f"{urlparse(endpoint_url).scheme}://{urlparse(endpoint_url).hostname}:{urlparse(endpoint_url).port}"


@router.post("/shorten", tags=["URLs"])
async def shorten(url_obj: Url, request: Request) -> Url:
    """
    Shorten the given long URL.
    :param request: request object
    :param url_obj: URL object
    :return: shortened URL.
    """
    suffix = hashlib.sha256(url_obj.url.encode("utf-8")).hexdigest()[:8]
    if suffix not in store:
        # store short-url-suffix: long-url into data store.
        store[suffix] = url_obj.url

    return Url(url=f"{_get_base_url(request.url_for('shorten'))}/{suffix}")


@router.get("/{suffix}", tags=["URLs"])
async def redirect(suffix: str) -> RedirectResponse:
    """
    Redirect to long URL for the given URL ID.
    :param suffix: URL ID for the corresponding long URL.
    :return: Long URL.
    """
    long_url = store[suffix]
    if long_url:
        # return permanent redirect so that browsers store this in their cache.
        response = RedirectResponse(url=long_url, status_code=301)
        return response
    raise HTTPException(status_code=404, detail="Short URL not found.")
