def find_common_participants(group1, group2, separator=','):
    participants_first_group = set(group1.split(separator))
    participants_second_group = set(group2.split(separator))

    common_participants = participants_first_group.intersection(participants_second_group)

    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)

participants_first_group2 = "Иванов,Петров,Сидоров"
participants_second_group2 = "Петров,Сидоров,Смирнов"

common_participants2 = find_common_participants(participants_first_group2, participants_second_group2, separator=',')
print(common_participants2)




