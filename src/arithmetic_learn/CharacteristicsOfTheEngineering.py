# coding=utf-8
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import OneHotEncoder
from numpy import vstack, array, nan
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr
#http://www.cnblogs.com/jasonfreak/p/5448385.html

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest

from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
# from minepy import MINE

from BasedOnThePenaltyItem import LR
#由于MINE的设计不是函数式的，定义mic方法将其为函数式的，返回一个二元组，二元组的第2项设置成固定的P值0.5
def mic(x, y):
    m = MINE()
    m.compute_score(x, y)
    return (m.mic(), 0.5)

# #选择K个最好的特征，返回特征选择后的数据
# SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)


def feature_prosessing():
    # 导入IRIS数据集
    iris = load_iris()
    # 特征矩阵
    print iris.data[:2] ,iris.target[:2]
    # 目标向量
    StandardScaler().fit_transform(iris.data)
    MinMaxScaler().fit_transform(iris.data)
    print Binarizer(threshold=3).fit_transform(iris.data)[:2],iris.target.reshape((-1,1))[:2]

    #dummy
    one_hot= OneHotEncoder()
    one_hot.fit(iris.target.reshape(-1, 1) )
    print one_hot.n_values ,one_hot.active_features_ ,one_hot.feature_indices_ ,one_hot.transform([[0]]).toarray()

    # 缺失值计算，返回值为计算缺失值后的数据
    # 参数missing_value为缺失值的表示形式，默认为NaN
    # 参数strategy为缺失值填充方式，默认为mean（均值）
    print Imputer().fit_transform(vstack((array([nan, nan, nan, nan]), iris.data))) [:2]

    print "PolynomialFeatures" , PolynomialFeatures().fit_transform(iris.data) [:4] ,len(PolynomialFeatures().fit_transform(iris.data) )
    print "VarianceThreshold", VarianceThreshold(threshold=1).fit_transform(iris.data) [:4] ,len(VarianceThreshold(threshold=1).fit_transform(iris.data)[0])

    # 选择K个最好的特征，返回选择特征后的数据
    # 第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，数组第i项为第i个特征的评分和P值。在此定义为计算相关系数
    # 参数k为选择的特征个数
    print iris.data[:2], iris.target[:2]
    # print SelectKBest(lambda X, Y: array(map(lambda x: pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data[:2], iris.target[:2])

    # 选择K个最好的特征，返回选择特征后的数据
    # print SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)

    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LogisticRegression

    # 递归特征消除法，返回特征选择后的数据
    # 参数estimator为基模型
    # 参数n_features_to_select为选择的特征个数
    print  RFE(estimator=LogisticRegression(), n_features_to_select=3).fit_transform(iris.data, iris.target) [:2]

    # 带L1惩罚项的逻辑回归作为基模型的特征选择
    print SelectFromModel(LogisticRegression(penalty="l1", C=0.1)).fit_transform(iris.data, iris.target) [:2]

    #L1惩罚项降维的原理在于保留多个对目标值具有同等相关性的特征中的一个，所以没选到的特征不代表不重要。故，可结合L2惩罚项来优化。具体操作为：
    # 若一个特征在L1中的权值为1， 选择在L2中权值差别不大且在L1中权值为0的特征构成同类集合，将这一集合中的特征平分L1中的权值，
    # 故需要构建一个新的逻辑回归模型
    # 带L1和L2惩罚项的逻辑回归作为基模型的特征选择
    # 参数threshold为权值系数之差的阈值
    print SelectFromModel(LR(threshold=0.5, C=0.1)).fit_transform(iris.data, iris.target)[:2]

    #基于树模型的特征选择法
    #树模型中GBDT也可用来作为基模型进行特征选择，使用feature_selection库的SelectFromModel类结合GBDT模型，来选择特征的代码如下：
    from sklearn.ensemble import GradientBoostingClassifier
    # GBDT作为基模型的特征选择
    print SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target) [:2]
if __name__ == '__main__':
    feature_prosessing()