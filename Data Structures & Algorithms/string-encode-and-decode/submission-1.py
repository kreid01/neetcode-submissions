class Solution:

    def encode(self, strs: List[str]) -> str:
        fin = ""
        for x in strs:
            fin += "#-" + x
        return fin

    def decode(self, s: str) -> List[str]:
        return s.split("#-")[1:]
        