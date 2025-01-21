# Problem: Return the maximum number of concurrent calls for a customer for a datetime range.
# Overlapping intervals problem.
# 1. Retrieve the list of all phone calls for a user.
# 2. Parse the phone records to into a python List: List[[start_time, end_time]...[n_start_time, n_end_time]]
# 3. Sort the python list by Start time.
# 4. Iterate through the list and push the end times onto a min heap.
# 4.5 If the min time is less than the current call start time pop the heap.
# 5. Keep track of the max length of the min heap.
# 6. Return max length of min heap after processing the call. 

