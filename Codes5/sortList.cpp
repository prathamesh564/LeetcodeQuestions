using namespace std;
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head) return nullptr;
        vector<int> nums;
        ListNode* curr=head;
        while(curr!=nullptr){
            nums.push_back(curr->val);
            curr=curr->next;
        }
        sort(nums.begin(),nums.end());
        curr=head;
        int i=0;
        while(curr!=nullptr){
            curr->val=nums[i];
            i++;
            curr=curr->next;
        }
        return head;
    }
};
