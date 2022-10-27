class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> answer;
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] != 0) answer.push_back(nums[i]);
        int i = 0;
        for (; i < answer.size(); i++) 
            nums[i] = answer[i];
        while (i < nums.size())
            nums[i++] = 0;
    }
};