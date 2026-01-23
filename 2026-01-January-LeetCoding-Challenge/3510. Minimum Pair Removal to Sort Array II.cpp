class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<long long> val(nums.begin(), nums.end());
        vector<int> left(n), right(n);
        vector<bool> alive(n, true);

        for (int i = 0; i < n; i++) {
            left[i] = i - 1;
            right[i] = (i + 1 < n ? i + 1 : -1);
        }

        // Min-heap: (sum, left_index)
        priority_queue<pair<long long,int>,
            vector<pair<long long,int>>,
            greater<>> pq;

        for (int i = 0; i + 1 < n; i++) {
            pq.push({val[i] + val[i + 1], i});
        }

        // Indices where order is violated
        set<int> bad;
        for (int i = 0; i + 1 < n; i++) {
            if (val[i] > val[i + 1]) bad.insert(i);
        }

        int ops = 0;

        while (!bad.empty()) {
            // Find valid minimum-sum adjacent pair
            auto [s, i] = pq.top(); pq.pop();
            if (!alive[i]) continue;
            int j = right[i];
            if (j == -1 || !alive[j]) continue;
            if (val[i] + val[j] != s) continue;

            // Merge i and j
            ops++;
            val[i] += val[j];
            alive[j] = false;

            int r = right[j];
            right[i] = r;
            if (r != -1) left[r] = i;

            // Remove outdated violations
            bad.erase(i);
            bad.erase(j);
            if (left[i] != -1) bad.erase(left[i]);
            if (r != -1) bad.erase(i);

            // Re-check local order
            if (left[i] != -1 && val[left[i]] > val[i])
                bad.insert(left[i]);
            if (r != -1 && val[i] > val[r])
                bad.insert(i);

            // Push new adjacent sums
            if (left[i] != -1)
                pq.push({val[left[i]] + val[i], left[i]});
            if (r != -1)
                pq.push({val[i] + val[r], i});
        }

        return ops;
    }
};
