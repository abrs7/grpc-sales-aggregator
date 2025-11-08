from backend.app.core.file_manager import new_upload_path, new_result_path, make_download_url

def test_paths_and_url():
    up = new_upload_path()
    res = new_result_path()
    assert up.name.startswith("upload_") and up.suffix == ".csv"
    assert res.name.startswith("result_") and res.suffix == ".csv"
    url = make_download_url(res.name)
    assert url.startswith("http://") and "/results/" in url
