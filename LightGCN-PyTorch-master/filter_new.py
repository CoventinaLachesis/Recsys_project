def process_file(file_path, output_file):
    total_interactions = 0
    u_interaction_counts = {}
    unique_U = set()
    interactions_limit = 100000

    u_mapping = {}
    next_u_id = 0

    with open(file_path, 'r') as file, open(output_file, 'w') as out_file:
        for line in file:
            # Split the line into integers
            numbers = list(map(int, line.split()))
            if len(numbers) > 1:
                U = numbers[0]  # First integer is U
                interactions = numbers[1:]  # Remaining integers are interactions

                # Skip U if it has fewer than 15 interactions
                if len(interactions) < 15:
                    continue

                # Map U to a new order
                if U not in u_mapping:
                    u_mapping[U] = next_u_id
                    next_u_id += 1
                mapped_U = u_mapping[U]

                # Count total interactions for each U
                if mapped_U not in u_interaction_counts:
                    u_interaction_counts[mapped_U] = 0
                u_interaction_counts[mapped_U] += len(interactions)

                # Add U to the unique set
                unique_U.add(mapped_U)

                # Count total interactions
                total_interactions += len(interactions)

                # Write filtered information with remapped U to the output file
                out_file.write(f"{mapped_U} " + " ".join(map(str, interactions)) + "\n")

                # Stop if we exceed or reach the limit
                if total_interactions >= interactions_limit:
                    break

    return total_interactions, len(unique_U), u_interaction_counts

# Example usage
# Example usage
file_path_train = 'train.txt'  # Replace with the actual path to your input file
output_file_train = 'filtered_train.txt'  # Replace with the desired output file path
interactions, unique_U_count, u_interaction_counts = process_file(file_path_train, output_file_train)
file_path_test = 'test.txt'  # Replace with the actual path to your input file
output_file_test = 'filtered_test.txt'  # Replace with the desired output file path
interactions, unique_U_count, u_interaction_counts = process_file(file_path_test, output_file_test)
print(f"Total interactions: {interactions}")
print(f"Unique interactions overall: {u_interaction_counts}")
print(f"Unique U count: {unique_U_count}")
print("Counts of interactions per mapped U:")