class ListNode(object):
    def __init__(self, x = None, next = None):
         self.val = x
         self.next = next

def isPalindrome(head):
    try: 
    	findMid = head
    	mid = head
    	if head.val == None:
    		raise Exception('Throw exception')
    	while findMid and findMid.next:
    		findMid = findMid.next.next
    		mid = mid.next
    	secondPart = []
    	while mid:
    		secondPart.append(mid.val)
    		mid = mid.next

    	while secondPart:
    		x = secondPart.pop()
    		if x != head.val:
    			return False
    		head = head.next
    	return True
    except Exception:
    	raise



test1 = ListNode('a',ListNode('b', ListNode('c', ListNode('c', ListNode('b', ListNode('a'))))))
print isPalindrome(test1)

test1 = ListNode('1',ListNode('1'))
print isPalindrome(test1)

test1 = ListNode('a', ListNode('b',ListNode('1', ListNode('2', ListNode('2', ListNode('1', ListNode('b', ListNode('a'))))))))
print isPalindrome(test1)

#print isPalindrome(ListNode())
