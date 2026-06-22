class Solution:

    def encode(self, strs: List[str]) -> str:
        output=""
        for word in strs:
            output+=(word)
            output+=("asdf")
        return output
    
    def decode(self, s: str) -> List[str]:
        inputs=s.split("asdf")
        return inputs[:-1]