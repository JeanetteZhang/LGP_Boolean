def make_mock_random(values):
    values.reverse()

    def mocked_random_choice(_):
        return values.pop()

    return mocked_random_choice