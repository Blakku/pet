from pet import InputExample
from pet.pvp import PVP

class AGNewsPVP(PVP):
    def get_parts(self,example: InputExample):
        """
        Return the parts for a given input example according to the pattern ID.
        """
        # Pattern 0: simple pass through
        if self.pattern_id == 0:
            parts_a = [example.text_a]
            parts_b = [example.text_b] if example.text_b else []
            return  parts_a, parts_b

        # Pattern 1 fix
        elif self.pattern_id == 1:
            parts_a = [example.text_a]
            parts_b = []
            if example.text_b:
                parts_b.append(example.text_b)
            return parts_a, parts_b

        elif self.pattern_id == 2:
            parts_a = [example.text_a, "This is related to ", example.text_b or ""]
            return parts_a, []

        elif self.pattern_id == 3:
            parts_a = ["Topic: ", example.text_a]
            parts_b = [example.text_b] if example.text_b else []
            return parts_a, parts_b
        else:
            raise ValueError(f"Unsupported pattern_id: {self.pattern_id}")

    def verbalize(self,label):
        mapping = {
            "0": ["World"],
            "1": ["Sports"],
            "2": ["Business"],
            "3": ["Science/Tech"]
        }
        return mapping.get(label,[])
