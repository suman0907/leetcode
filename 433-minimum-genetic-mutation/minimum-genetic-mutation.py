class Solution:
    """
    time_complexity: o(n) n= size of bank
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank = set(bank)
        qu = [(startGene,0)]
        while qu:
            curr, count = qu.pop(0)
            if curr==endGene:
                return count
            for i, ch in enumerate(curr):
                for new_ch in "ACGT":
                    mut_gene = curr[:i]+new_ch+curr[i+1:]
                    if mut_gene in bank:
                        qu.append((mut_gene,count+1))
                        bank.remove(mut_gene)
        return -1                    
