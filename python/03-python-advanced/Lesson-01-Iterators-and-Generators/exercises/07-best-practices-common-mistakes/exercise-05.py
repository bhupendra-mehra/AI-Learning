#When should you use a list?
# The dataset is small, random access (numbers[5]), iterate over the data multiple times.
# ,list-specific methods such as append(), sort(), or reverse().
#When should you use a generator?
#Processing large datasets. Reading large files. Streaming API responses. Processing database records. Building data pipelines.Memory efficiency is important.
# When should you create a custom iterator?
#Complex iteration logic is required. complete control over iteration. building reusable iterator classes.custom behavior or state.