from login import get_post
import pytest

def test_step1(login):
    res = get_post(login)
    res_list = res.get("data")
    res_id_list = [item['id'] for item in res_list]
    assert  1234 in res_id_list, "тест не пройден"


if __name__ == '__main__':
    pytest.main(["-vv"])
