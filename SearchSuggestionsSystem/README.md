# SearchSuggestionsSystem

## Problem Description
You are given an array of strings products and a string searchWord.<br>

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.<br>

Return a list of lists of the suggested products after each character of searchWord is typed.<br>

## Examples
### Example 1
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"<br>
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]<br>
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].<br>
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].<br>
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].<br>

### Example 2
Input: products = ["havana"], searchWord = "havana"<br>
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]<br>
Explanation: The only word "havana" will be always suggested while typing the search word.<br>

## Constraints
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 10^4
- All the strings of products are unique.
- products[i] consists of lowercase English letters.
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters.

## Solution
```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        suggestions = []
        products = sorted(products)
        for end in range(0, len(searchWord)):
            suggestion = []
            for product in products:
                if len(suggestion) == 3: break
                if product.startswith(searchWord[:end+1]):
                    suggestion.append(product)
            suggestions.append(suggestion)
        return suggestions
```

## Leetcode Link
[Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)
