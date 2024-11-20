def process_file(file_path, output_file):
    total_interactions = 0
    u_interaction_counts = {}
    unique_interactions = set()
    interactions_limit = 100000

    interaction_mapping = {}
    u_mapping = {}
    next_interaction_id = 1
    next_u_id = 1

    with open(file_path, 'r') as file, open(output_file, 'w') as out_file:
        for line in file:
            # Split the line into integers
            numbers = list(map(int, line.split()))
            if len(numbers) > 1:
                U = numbers[0]  # First integer is U
                interactions = numbers[1:]  # Remaining integers are interactions

                # Skip U if it has fewer than 200 interactions
                if len(interactions) < 200:
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

                # Map interactions to a new order
                mapped_interactions = []
                for interaction in interactions:
                    if interaction not in interaction_mapping:
                        interaction_mapping[interaction] = next_interaction_id
                        next_interaction_id += 1
                    mapped_interactions.append(interaction_mapping[interaction])

                # Add mapped interactions to the unique set
                unique_interactions.update(mapped_interactions)

                # Count total interactions
                total_interactions += len(interactions)

                # Write filtered information with new order to the output file
                out_file.write(f"{mapped_U} " + " ".join(map(str, mapped_interactions)) + "\n")

                # Stop if we exceed or reach the limit
                if total_interactions >= interactions_limit:
                    break

    return total_interactions, len(unique_interactions), len(u_mapping), u_interaction_counts

# Example usage
file_path = 'train.txt'  # Replace with the actual path to your input file
output_file = 'filtered_train.txt'  # Replace with the desired output file path
interactions, unique_interaction_count, unique_U_count, u_interaction_counts = process_file(file_path, output_file)

print(f"Total interactions: {interactions}")
print(f"Unique interactions overall: {unique_interaction_count}")
print(f"Unique U count: {unique_U_count}")
print("Counts of interactions per mapped U:")
for mapped_U, count in u_interaction_counts.items():
    print(f"Mapped U = {mapped_U}, Total Interactions = {count}")
