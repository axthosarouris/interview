from assertpy import assert_that

from hello_poetry.hello import message


def should_return_hello():
    assert_that(message()).is_equal_to("hello!")


