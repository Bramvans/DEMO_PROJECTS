#!/usr/bin/env python
# coding: utf-8

# In[67]:


### Verwijder Na regels opm basis van kolom
def remove_na_by_column(df, column):
        """Verwijdert NaN waarden per kolom (DF, "KOLOM") een lijst kolommen is mogelijk"""
        a = df.dropna(subset=[column])
        return a


# In[68]:


### Tel het aantal unieke waarden per kolom
def count_distinct_values_column(df, column):
    """Unieke waarden per colum (DF , "KOLOM") Lijst kolommen is mogelijk."""
    return df[column].nunique()


# In[89]:


### Voeg alle colomnamen toe aan een lijst
def column_list(df):
    """Voegt alle colom namen toe aan een lijst """
    columns = []
    for colum in df.columns:
        columns.append(colum)
    #columns = pd.DataFrame(columns)
    return columns


# In[204]:


### Groepeer en gemiddelde
def group_by_mean_median(df, group, mean):
    """Groepeer by colom en geeft het gemiddelde & mediaan terug """
    a = df.dropna()
    b = a.groupby(group)[mean].mean().reset_index().round(1)
    c = a.groupby(group)[mean].median().reset_index().round(1)
    return pd.merge(b, c, left_on= group, right_on= group)


# In[200]:


### Aantal waardes per column
def values_by_column(df, column):
    """Aantal gevulde waarden per column exclusief na waarde"""
    a = remove_na_by_column(df, column)
    return a[column].shape[0]


# In[201]:


### Aantal rijen in de data set
def number_of_rows(df):
    """Aantal rijen in de dataset, inclusief Na waarden"""
    return df.shape[0]

