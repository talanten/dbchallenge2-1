
class Tokenizer(object):
    def parse_string(self, tags):
        result = []

        if(len(tags) > 1):
            if(tags[0] == "," or tags[0] == " "):
                tags = tags[1:]
            if(tags[-1] == "," or tags[-1] == " "):
                tags = tags[:-1]
            result = tags.split(", ")
        return result