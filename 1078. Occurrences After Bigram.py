'''Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".'''

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        result = []

        if len(text) < 3:
            return result

        else:
            queue = [text[0], text[1]]
            for word in text[2:]:
                if queue and queue[-1] == second and queue[-2] == first:
                    result.append(word)
                    queue.append(word)
                    queue.pop(0)

                else:
                    queue.append(word)
                    queue.pop(0)

        return result
