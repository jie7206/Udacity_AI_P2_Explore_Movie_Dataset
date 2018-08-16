
# coding: utf-8

# ## 探索电影数据集
# 
# 在这个项目中，你将尝试使用所学的知识，使用 `NumPy`、`Pandas`、`matplotlib`、`seaborn` 库中的函数，来对电影数据集进行探索。
# 
# 下载数据集：
# [TMDb电影数据](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/explore+dataset/tmdb-movies.csv)
# 

# 
# 数据集各列名称的含义：
# <table>
# <thead><tr><th>列名称</th><th>id</th><th>imdb_id</th><th>popularity</th><th>budget</th><th>revenue</th><th>original_title</th><th>cast</th><th>homepage</th><th>director</th><th>tagline</th><th>keywords</th><th>overview</th><th>runtime</th><th>genres</th><th>production_companies</th><th>release_date</th><th>vote_count</th><th>vote_average</th><th>release_year</th><th>budget_adj</th><th>revenue_adj</th></tr></thead><tbody>
#  <tr><td>含义</td><td>编号</td><td>IMDB 编号</td><td>知名度</td><td>预算</td><td>票房</td><td>名称</td><td>主演</td><td>网站</td><td>导演</td><td>宣传词</td><td>关键词</td><td>简介</td><td>时常</td><td>类别</td><td>发行公司</td><td>发行日期</td><td>投票总数</td><td>投票均值</td><td>发行年份</td><td>预算（调整后）</td><td>票房（调整后）</td></tr>
# </tbody></table>
# 

# **请注意，你需要提交该报告导出的 `.html`、`.ipynb` 以及 `.py` 文件。**

# 
# 
# ---
# 
# ---
# 
# ## 第一节 数据的导入与处理
# 
# 在这一部分，你需要编写代码，使用 Pandas 读取数据，并进行预处理。

# 
# **任务1.1：** 导入库以及数据
# 
# 1. 载入需要的库 `NumPy`、`Pandas`、`matplotlib`、`seaborn`。
# 2. 利用 `Pandas` 库，读取 `tmdb-movies.csv` 中的数据，保存为 `movie_data`。
# 
# 提示：记得使用 notebook 中的魔法指令 `%matplotlib inline`，否则会导致你接下来无法打印出图像。

# In[1]:


# 载入需要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 设定能在 notebook 打印出图像
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# 利用 Pandas 库，读取 tmdb-movies.csv 中的数据，保存为 movie_data
movie_data = pd.read_csv('./tmdb-movies.csv')


# ---
# 
# **任务1.2: ** 了解数据
# 
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
# 
# 1. 获取数据表的行列，并打印。
# 2. 使用 `.head()`、`.tail()`、`.sample()` 方法，观察、了解数据表的情况。
# 3. 使用 `.dtypes` 属性，来查看各列数据的数据类型。
# 4. 使用 `isnull()` 配合 `.any()` 等方法，来查看各列是否存在空值。
# 5. 使用 `.describe()` 方法，看看数据表中数值型的数据是怎么分布的。
# 
# 

# In[3]:


# 1.获取数据表的行列，并打印
print("此电影数据表共有 {} 行 {} 列".format(movie_data.shape[0],movie_data.shape[1]))


# In[4]:


# 2-1.使用 .head() 方法，观察、了解数据表的情况
movie_data.head()


# In[5]:


# 2-2.使用 tail() 方法，观察、了解数据表的情况
movie_data.tail()


# In[6]:


# 2-3.使用 sample() 方法，观察、了解数据表的情况
movie_data.sample()


# In[7]:


# 3.使用 .dtypes 属性，来查看各列数据的数据类型。
movie_data.dtypes


# In[8]:


# 4.使用 isnull() 配合 .any() 等方法，来查看各列是否存在空值。
movie_data.isnull().any()


# In[9]:


# 5.使用 .describe() 方法，看看数据表中数值型的数据是怎么分布的。
movie_data.describe()


# ---
# 
# **任务1.3: ** 清理数据
# 
# 在真实的工作场景中，数据处理往往是最为费时费力的环节。但是幸运的是，我们提供给大家的 tmdb 数据集非常的「干净」，不需要大家做特别多的数据清洗以及处理工作。在这一步中，你的核心的工作主要是对数据表中的空值进行处理。你可以使用 `.fillna()` 来填补空值，当然也可以使用 `.dropna()` 来丢弃数据表中包含空值的某些行或者列。
# 
# 任务：使用适当的方法来清理空值，并将得到的数据保存。

# In[10]:


movie_data = movie_data.dropna().reset_index()
print("丢弃空值后，此电影数据表共有 {} 行".format(movie_data.shape[0]))


# ---
# 
# ---
# 
# ## 第二节 根据指定要求读取数据
# 
# 
# 相比 Excel 等数据分析软件，Pandas 的一大特长在于，能够轻松地基于复杂的逻辑选择合适的数据。因此，如何根据指定的要求，从数据表当获取适当的数据，是使用 Pandas 中非常重要的技能，也是本节重点考察大家的内容。
# 
# 

# ---
# 
# **任务2.1: ** 简单读取
# 
# 1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
# 2. 读取数据表中前1～20行以及48、49行的数据。
# 3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
# 
# 要求：每一个语句只能用一行代码实现。

# In[11]:


# 1.读取数据表中名为 id、popularity、budget、runtime、vote_average 列的数据
movie_data[['id', 'popularity', 'budget', 'runtime', 'vote_average']]


# In[12]:


# 2-1.读取数据表中前1～20行的数据
movie_data[:20]


# In[13]:


# 2-2.读取数据表中48、49行的数据
movie_data[47:49]


# In[14]:


# 3.读取数据表中第50～60行的 popularity 那一列的数据
movie_data[['popularity']][49:60]


# ---
# 
# **任务2.2: **逻辑读取（Logical Indexing）
# 
# 1. 读取数据表中 **`popularity` 大于5** 的所有数据。
# 2. 读取数据表中 **`popularity` 大于5** 的所有数据且**发行年份在1996年之后**的所有数据。
# 
# 提示：Pandas 中的逻辑运算符如 `&`、`|`，分别代表`且`以及`或`。
# 
# 要求：请使用 Logical Indexing实现。

# In[15]:


# 1.读取数据表中 popularity 大于5 的所有数据
movie_data[movie_data['popularity'] > 5]


# In[16]:


# 2.读取数据表中 popularity 大于5 的所有数据且发行年份在1996年之后的所有数据
movie_data[(movie_data['popularity'] > 5) & (movie_data['release_year'] >= 1996)]


# ---
# 
# **任务2.3: **分组读取
# 
# 1. 对 `release_year` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `revenue` 的均值。
# 2. 对 `director` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `popularity` 的均值，从高到低排列。
# 
# 要求：使用 `Groupby` 命令实现。

# In[17]:


# 1.对 release_year 进行分组，使用 .agg 获得 revenue 的均值
movie_data.groupby(['release_year']).agg({'revenue':'mean'})


# In[18]:


# 2.对 director 进行分组，使用 .agg 获得 popularity 的均值，从高到低排列。
movie_data.groupby(['director']).agg({'popularity':'mean'}).sort_values(['popularity'],ascending=False)


# ---
# 
# ---
# 
# ## 第三节 绘图与可视化
# 
# 接着你要尝试对你的数据进行图像的绘制以及可视化。这一节最重要的是，你能够选择合适的图像，对特定的可视化目标进行可视化。所谓可视化的目标，是你希望从可视化的过程中，观察到怎样的信息以及变化。例如，观察票房随着时间的变化、哪个导演最受欢迎等。
# 
# <table>
# <thead><tr><th>可视化的目标</th><th>可以使用的图像</th></tr></thead><tbody>
#  <tr><td>表示某一属性数据的分布</td><td>饼图、直方图、散点图</td></tr>
#  <tr><td>表示某一属性数据随着某一个变量变化</td><td>条形图、折线图、热力图</td></tr>
#  <tr><td>比较多个属性的数据之间的关系</td><td>散点图、小提琴图、堆积条形图、堆积折线图</td></tr>
# </tbody></table>
# 
# 在这个部分，你需要根据题目中问题，选择适当的可视化图像进行绘制，并进行相应的分析。对于选做题，他们具有一定的难度，你可以尝试挑战一下～

# **任务3.1：**对 `popularity` 最高的20名电影绘制其 `popularity` 值。

# In[19]:


# 找出popularity值最高的20名电影
sort_by_popularity = movie_data[['popularity','release_year','revenue']].set_index('popularity').sort_index(ascending=False).reset_index()
top20df = sort_by_popularity[:20]
top20df


# In[20]:


# 查看数据最大值与最小值以便找出绘图时bins的边界值
top20df.describe()


# In[21]:


# 绘制热图以查看知名度与发行年份的关系
plt.figure(figsize=[18,8])
bins_x = np.arange(8, 33+0.5, 0.5)
bins_y = np.arange(1977, 2015+2, 1)
h2d = plt.hist2d(data = top20df, x = 'popularity', y = 'release_year', bins = [bins_x, bins_y], cmap = 'viridis_r', cmin = 0.5);
counts = h2d[0]
plt.colorbar();
plt.xticks(bins_x,["{:0.1f}".format(x) for x in bins_x],rotation=45)
plt.yticks(bins_y,bins_y)
plt.xlabel('Popularity');
plt.ylabel('Release Year');
# 为每个热图的格子添加计数值
for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        c = counts[i,j]
        if c >= 2:
            plt.text(bins_x[i]+0.25, bins_y[j]+0.4, int(c), ha = 'center', va = 'center', color = 'white')
        elif c > 0:
            plt.text(bins_x[i]+0.25, bins_y[j]+0.4, int(c), ha = 'center', va = 'center', color = 'black')


# **分析结果**：由知名度与发行年份的热图可知，知名度排行前20名的电影大部分都在**2014**及**2015**年，值得注意的是**1977**年的那部电影，尽管年代久远，排名度却在前20名内。

# In[22]:


# 绘制散点图以查看知名度与票房的关系
plt.figure(figsize = [15,5])
plt.scatter(data = top20df, x= 'popularity', y = 'revenue', alpha = 0.5);
plt.xlabel('Popularity');
plt.ylabel('Revenue');


# **分析结果**：由知名度与票房的散点图可知，知名度最高的电影不一定票房最高。

# ---
# **任务3.2：**分析电影净利润（票房-成本）随着年份变化的情况，并简单进行分析。

# In[23]:


# 设定电影净利润(net_profit)数据集
movie_data['net_profit'] = movie_data['revenue'] - movie_data['budget_adj']
movie_data.sample()


# In[24]:


# 取出最近10年内的电影数据以进行分析
last10y = movie_data[movie_data['release_year'] > 2005]
last10y.sample()


# In[25]:


print("最近10年内的电影数据共有 {} 行 {} 列".format(last10y.shape[0],last10y.shape[1]))


# In[26]:


# 以小提琴图与箱线图显示电影净利润（票房-成本）随着年份变化的情况
base_color = sb.color_palette()[0]
plt.figure(figsize = [15, 6])
plt.subplot(1,2,1)
sb.violinplot(data = last10y, x = 'release_year', y = 'net_profit', color = base_color);
plt.subplot(1,2,2)
sb.boxplot(data = last10y, x = 'release_year', y = 'net_profit', color = base_color);


# **分析结果：**由小提琴图与箱线图来显示电影净利润随着年份变化的情况并不是很清楚，小提琴图的须子大部分拖得很长，因此中位数的变化看起来都差不多，箱线图也是，很多超出范围之外的异常值，因此，我打算使用电影净利润的平均值来查看，也就是使用条形图和折线图的方法来分析电影净利润（票房-成本）随着年份变化的情况。

# In[27]:


# 以条形图和折线图来显示数据的变化
plt.figure(figsize = [15, 4])
plt.subplot(1,2,1)
sb.barplot(data = last10y, x = 'release_year', y = 'net_profit', color = base_color);
plt.ylabel('Avg. Net Profit');
plt.subplot(1,2,2)
sb.pointplot(data = last10y, x = 'release_year', y = 'net_profit', errwidth='0');
plt.ylabel('Avg. Net Profit');


# **分析结果：**由条形图与折线图来显示电影净利润的平均值随年份变化的情形就很清楚了，尤其是位于右方的折线图更加直观明了，我们可以看到，随着时间的推移，整体来看，电影的净利润是成一路上升走势，最高点在最后的一年(2015)，虽然2008年和2010这两年的利润都比上一年下滑，以及2013、2014连续两年下滑，不过，很快的，到了2015年创下10年来最高纪录，因此，整体的走势还是一路向上的。

# ---
# 
# **[选做]任务3.3：**选择最多产的10位导演（电影数量最多的），绘制他们排行前3的三部电影的票房情况，并简要进行分析。

# ---
# 
# **[选做]任务3.4：**分析1968年~2015年六月电影的数量的变化。

# ---
# 
# **[选做]任务3.5：**分析1968年~2015年六月电影 `Comedy` 和 `Drama` 两类电影的数量的变化。

# > 注意: 当你写完了所有的代码，并且回答了所有的问题。你就可以把你的 iPython Notebook 导出成 HTML 文件。你可以在菜单栏，这样导出**File -> Download as -> HTML (.html)、Python (.py)** 把导出的 HTML、python文件 和这个 iPython notebook 一起提交给审阅者。
