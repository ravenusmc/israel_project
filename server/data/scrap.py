    # # I need to break this down by selected group - Israeli's and Palestinians 
    # def deaths_of_people_took_part_in_event(self, year):
    #     df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
    #     df_filtered_citizenship = df_filtered[df_filtered['citizenship'] == 'Palestinian']
    #     columns = ['Participated', 'Count']
    #     took_part_list = ['Yes', 'No']
    #     for item in took_part_list:
    #         rows = []
    #         rows.append(item)
    #         df_filtered_took_part = df_filtered_citizenship[df_filtered_citizenship['took_part_in_the_hostilities'] == item]
    #         count = len(df_filtered_took_part)
    #         rows.append(count)
    #         columns.append(rows)
    #     return columns 

    # def common_ammunition_used(self, year):
    #     data = []
    #     columns = ['Type of Ammunition', 'Palestinian Count', 'Israeli Count']
    #     data.append(columns)
    #     df_filtered_by_year  = self.data[self.data['date_of_death'].dt.year <= year]
    #     type_of_ammunition = ['live ammunition', 'missile', 'rocket', '0.22-caliber bullets', 'bomb', 
    #      'knife', 'shell', 'rock', 'rubber-coated metal bullets', 'stun grenade', 
    #      'teargas canister', 'flare bomb', 'sponge rounds', 'mortar fire', 'grad rocket', 
    #      'flechette shells', 'phosphorus shell', 'Qassam rocket', 'explosive belt', 
    #      'grenade', 'car bomb']
    #     for ammo in type_of_ammunition: 
    #         df_filtered_palestinian = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Palestinian']
    #         df_filtered_israeli = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Israeli']
    #         p_count_df = df_filtered_palestinian[df_filtered_palestinian['ammunition'] == ammo]
    #         i_count_df = df_filtered_israeli[df_filtered_israeli['ammunition'] == ammo]
    #         p_count = len(p_count_df)
    #         i_count = len(i_count_df)
    #         data.append([ammo, p_count, i_count])
    #     return data 