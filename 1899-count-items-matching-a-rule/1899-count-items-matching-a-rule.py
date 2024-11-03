class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rule_index={"type":0, "color":1, "name":2}
        return(sum(1 for item in items if item[rule_index[ruleKey]]==ruleValue))


        