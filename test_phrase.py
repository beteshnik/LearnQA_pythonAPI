class TestExamples:
    def test_phrase(self):
        expected_phrase_size = 15
        phrase = input(f"Введите фразу с количеством символов, не превышающим {expected_phrase_size}\n")
        len_phrase = len(phrase)
        assert len_phrase <= expected_phrase_size,\
            f"Вы ввели фразу с количеством символов {len_phrase}, превышающим {expected_phrase_size}"
