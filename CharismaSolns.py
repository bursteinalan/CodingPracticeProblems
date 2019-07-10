def problem1(n):

        #base case
        if n <= 3:
                return n
        
        #max perf squares
        ans = n

        #breaking down and finding min perf squares
        for i in range(1,n+1):
                
                temp = i * i;
                if temp > n:
                        break
                else:
                        ans = min(ans, 1 +problem1(n-temp))

        return ans;


def problem2(digits):

        #phone layout
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
        
        #empty array to hold all combos
        all_combos = ['']


        for digit in digits:
            curr_combo = list()
            
            for letter in phone[digit]:
                    
                for combo in all_combos: 
                    curr_combo.append(combo + letter)
                    
            all_combos = curr_combo
            
        return all_combos

def main():
	# p1_1 = problem1(12)
	# p1_2 = problem1(13)
	# print('p1_1 should be 3 and is:',p1_1)
	# print('p1_2 should be 2 and is:',p1_2)
        p2_1 = problem2("23")
        p2_1_ans = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        print('p2_1 should be ',p2_1_ans,' and is:',p2_1)
main()
