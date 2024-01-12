#!/usr/bin/env python
# coding: utf-8

# # Data Exploration

# In[2]:


import pandas as pd
import plotly.express as px


# Import the data base

# In[3]:


path = r"../litology_exploration/Data/texture.csv"
df_geo = pd.read_csv(path, sep=",")
df_geo.head()


# In[4]:


df = df_geo.fillna(0)
df.head()


# In[50]:


fig = px.scatter_mapbox(
                        df, lat="LATITUDE",
                        lon="LONGITUDE",
                        hover_name="AREA",
                        hover_data="LITHOLOGY",
                        zoom=2,
                        height=500
                        )
fig.update_layout(
                    mapbox_style="white-bg",mapbox_layers=[
                        {
                            "below": 'traces',
                            "sourcetype": "raster",
                            "sourceattribution": "United States Geological Survey",
                            "source": [
                                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                            ]
                        }
                    ]
                )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[29]:


fig = px.scatter_3d(
                    df, x='LONGITUDE',
                    y='LATITUDE',
                    z='DEPTH_M',
                    color='LITHOLOGY'
                    )
fig.show()


# In[9]:


Areas = df_geo['AREA'].unique()
Areas


# In[18]:


fig = px.bar(df_geo['AREA'], color_discrete_sequence=['blue'])
fig.update_layout(
                    autosize=True,
                    width=1000,
                    height=1000
                    )
fig.show()


# We are going to choose the Area "NEW ENGLAND"

# In[62]:


df_NEW_ENGLAND = df_geo[df_geo["AREA"] == "NEW ENGLAND"]
df_NEW_ENGLAND.head()


# In[45]:


fig = px.scatter_mapbox(
                        df_NEW_ENGLAND, lat="LATITUDE",
                        lon="LONGITUDE",
                        hover_name="AREA",
                        hover_data="CLASSIFICATION",
                        zoom=7,
                        height=500
                        )
fig.update_layout(
                    mapbox_style="white-bg",mapbox_layers=[
                        {
                            "below": 'traces',
                            "sourcetype": "raster",
                            "sourceattribution": "United States Geological Survey",
                            "source": [
                                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                            ]
                        }
                    ]
                )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[30]:


df_NEW_ENGLAND.describe()


# In[31]:


df_NEW_ENGLAND.columns


# In[32]:


df_NEW_ENGLAND["CLASSIFICATION"].unique()


# In[33]:


df_NEW_ENGLAND["LITHOLOGY"].unique()


# We can see that the LITHOLOGY columns doesn't have data, that's why we are going to work with GRAVEL_PCT, SAND_PCT, SILT_PCT AND CLAY_PCT, to verify the CLASSIFICATION

# In[42]:


fig = px.scatter_ternary(
                        df_NEW_ENGLAND,
                        a = 'SAND_PCT',
                        b = 'SILT_PCT',
                        c = 'CLAY_PCT',
                        color = "CLASSIFICATION",
                        size = "WEIGHT",
                        size_max = 10
                        )

fig.show()


# In[63]:


df_NEW_ENGLAND = df_NEW_ENGLAND.query("DEPTH_M > -9")


# In[64]:


fig = px.scatter_3d(
                    df_NEW_ENGLAND,
                    x='LONGITUDE',
                    y='LATITUDE',
                    z='DEPTH_M',
                    color='CLASSIFICATION'
                    )
fig.show()


# Plot other data, the info from the AREA "CHESAPEAKE BAY"

# In[87]:


df_CHESAPEAKE_BAY = df_geo[df_geo["AREA"] == "CHESAPEAKE BAY"]
df_CHESAPEAKE_BAY.head()


# In[88]:


fig = px.scatter_mapbox(
                        df_CHESAPEAKE_BAY, lat="LATITUDE",
                        lon="LONGITUDE",
                        hover_name="AREA",
                        hover_data="LITHOLOGY",
                        zoom=7,
                        height=500
                        )
fig.update_layout(
                    mapbox_style="white-bg",mapbox_layers=[
                        {
                            "below": 'traces',
                            "sourcetype": "raster",
                            "sourceattribution": "United States Geological Survey",
                            "source": [
                                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                            ]
                        }
                    ]
                )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[89]:


df_CHESAPEAKE_BAY["CLASSIFICATION"].unique()


# In[90]:


df_CHESAPEAKE_BAY["LITHOLOGY"].unique()


# As we can see, the CLASSIFICATION is easer to analyze than the LITHOLOGY

# In[91]:


df_CHESAPEAKE_BAY["WEIGHT"].describe()


# In[92]:


df_CHESAPEAKE_BAY_ = df_CHESAPEAKE_BAY.query("WEIGHT > 0")


# In[83]:


fig = px.scatter_ternary(
                        df_CHESAPEAKE_BAY_,
                        a = 'SAND_PCT',
                        b = 'SILT_PCT',
                        c = 'CLAY_PCT',
                        color = "CLASSIFICATION",
                        size = "WEIGHT",
                        size_max = 10
                        )

fig.show()


# In[93]:


df_CHESAPEAKE_BAY = df_CHESAPEAKE_BAY.query("DEPTH_M > 0")


# In[94]:


fig = px.scatter_3d(
                    df_CHESAPEAKE_BAY,
                    x='LONGITUDE',
                    y='LATITUDE',
                    z='DEPTH_M',
                    color='CLASSIFICATION'
                    )
fig.show()

