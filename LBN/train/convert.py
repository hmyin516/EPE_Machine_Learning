import h5py
import pandas as pd 
import numpy as np 
import os


print(os.getcwd())
path = "LBN/data/five-class"


features = ["j1_e","j1_px","j1_py","j1_pz"]
j_index = ["j_index"]
labels = ['j_q', 'j_g', 'j_w', 'j_z', 'j_t']


columns = []
for i in range(50):
    columns.append("E_" + str(i))
    columns.append("PX_" + str(i))
    columns.append("PY_" + str(i))
    columns.append("PZ_" + str(i))
columns.append("is_signal_q")
columns.append("is_signal_g")
columns.append("is_signal_w")
columns.append("is_signal_z")
columns.append("is_signal_t")
columns.append("j_index")

for filename in os.listdir(path):

    f = h5py.File(path + "/" + filename, 'r')
    treeArray = f['t_allpar_new'][()]
    f.close()

    df = pd.DataFrame(treeArray,columns=list(set(features+j_index)))
    df = df.drop_duplicates()
    df = df[features+j_index]
    df2 = (df.pivot_table(index = "j_index", columns = df.groupby("j_index").cumcount().add(1), aggfunc = "first", fill_value = 0).sort_index(axis = 1, level = 1))
    df2 = (df2.set_axis([f'{x}{y}' for x,y in df2.columns], axis=1).reset_index())
    df2 = df2.iloc[:, 1:201]
    df2.reset_index(drop = True, inplace = True)

    if(len(df2.columns) < 200):
        i = int(len(df2.columns) / 4)
        length = df2.shape[0]
        while i <= 50:
            df2["j1_e" + str(i)] = np.zeros((length))
            df2["j1_px" + str(i)] = np.zeros((length))
            df2["j1_py" + str(i)] = np.zeros((length))
            df2["j1_pz" + str(i)] = np.zeros((length))
            i = i + 1
    features_np = np.stack((treeArray["j_q"], treeArray["j_g"], treeArray["j_w"], treeArray["j_z"], treeArray["j_t"], treeArray["j_index"]))
    features_df = pd.DataFrame(features_np.T, columns = ["j_q", "j_g", "j_w", "j_z", "j_t", "j_index"])
    features_df = features_df.drop_duplicates()
    features_df.sort_values(by=["j_index"], inplace=True)
    # features_df = features_df.iloc[:, :-1]
    features_df.reset_index(drop = True, inplace = True)

    df_final = pd.concat([df2, features_df], axis=1)
    df_final["j_q"] = df_final["j_q"].astype(int)
    df_final["j_g"] = df_final["j_g"].astype(int)
    df_final["j_w"] = df_final["j_w"].astype(int)
    df_final["j_z"] = df_final["j_z"].astype(int)
    df_final["j_t"] = df_final["j_t"].astype(int)
    df_final["j_index"] = df_final["j_index"].astype(int)
    df_final.columns = columns
    
    np_dat = df_final.to_numpy()
    np_x =  np_dat[:,:200]
    np_y = np_dat[:,200:-1]
    np_x = np_x.reshape((-1,50,4))
    np_y = np_y.astype('int32')
   
    #df_final.to_hdf('LBN/data/converted/' + filename + '.h5', key='table', mode='w', format='table')
    h5f_x = h5py.File('LBN/data/converted/np/' + filename + '_x.h5','w')
    h5f_x.create_dataset('data',data = np_x)
    h5f_x.close()
    h5f_y = h5py.File('LBN/data/converted/np/' + filename + '_y.h5','w')
    h5f_y.create_dataset('data',data = np_y)
    h5f_y.close()
    print(filename + " written")