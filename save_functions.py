

def save_cleaning_steps(base_dir, folder_name, args):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['Text Cleaning Schritte', args]
    with open(base_dir + folder_name + "/Cleaning_steps.txt", "w") as text_file:
        for line in lines:
            text_file.write(line)
            text_file.write('\n')
        text_file.close()

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_count_vectorizer_parameters(base_dir, folder_name, parameters):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['Count Vectorizer Parameters', parameters]
    with open(base_dir + folder_name + "/Count_Vectorizer_parameters.txt", "w") as text_file:
        for line in lines:
            text_file.write(line)
            text_file.write('\n')
        text_file.close()


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_count_vectorizer_CV_results(base_dir, folder_name, estimators, param_grid, result_df):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['Estimators', estimators, 'Parameter Grid', param_grid, 'Resultat', result_df]
    with open(base_dir + folder_name + "/Count_Vectorizer_CV_results.txt", "w") as text_file:
        for line in lines:
            text_file.write(line)
            text_file.write('\n')
            text_file.write('\n')
        text_file.close()

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_test_prediction(base_dir, folder_name, file_name, model, conf_matrix, report):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['Model', model, 'Confusion Matrix', conf_matrix, 'Report', report]
    if not os.path.exists(base_dir + folder_name + file_name+ ".txt"):
        with open(base_dir + folder_name + file_name+ ".txt", "w") as text_file:
            for line in lines:
                text_file.write(line)
                text_file.write('\n')
                text_file.write('\n')
            text_file.close()
    else:
        with open(base_dir + folder_name + file_name+ ".txt", "a") as text_file:
            for line in lines:
                text_file.write(line)
                text_file.write('\n')
                text_file.write('\n')
            text_file.close()  

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_tfidf_vectorizer_parameters(base_dir, folder_name, parameters):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['TFIDF Vectorizer Parameters', parameters]
    with open(base_dir + folder_name + "/TFIDF_Vectorizer_parameters.txt", "w") as text_file:
        for line in lines:
            text_file.write(line)
            text_file.write('\n')
        text_file.close()

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_tfidf_vectorizer_CV_results(base_dir, folder_name, estimators, param_grid, result_df):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['Estimators', estimators, 'Parameter Grid', param_grid, 'Resultat', result_df]
    with open(base_dir + folder_name + "/TFIDF_Vectorizer_CV_results.txt", "w") as text_file:
        for line in lines:
            text_file.write(line)
            text_file.write('\n')
            text_file.write('\n')
        text_file.close()

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_NN_summary(base_dir, folder_name, model, filename):
    from contextlib import redirect_stdout
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    # lines = ['NN Summary', summary]
    with open(base_dir + folder_name + filename+".txt", "w") as text_file:
        # for line in lines:
        #     text_file.write(line)
        #     text_file.write('\n')
        #     text_file.write('\n')
        with redirect_stdout(text_file):
            model.summary()
        text_file.close()

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_NN_result(base_dir, folder_name, result, filename):
    import os
    # Überprüfe ob Ordner existiert
    isExist = os.path.exists(base_dir + folder_name)

    if not isExist:
        # Erstelle ein neuer Ordner
        os.makedirs(base_dir + folder_name)
        print("Neuer Ordner wurde erstellt!")
    
    # Speichere die Parameter als text file
    lines = ['NN Result', result]
    with open(base_dir + folder_name + filename+".txt", "w") as text_file:
        for line in lines:
            text_file.write(line)
            text_file.write('\n')
            text_file.write('\n')
        text_file.close()

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_wrong_predictions(y_test, y_pred, base_dir, folder_name,  filename):
    import pickle
    true_false = y_test==y_pred
    wrong_pred_index = list(true_false[true_false == False].index)
    with open(base_dir + folder_name+ filename + '.pickle', 'wb') as f:
        pickle.dump(wrong_pred_index, f)

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def save_test_pred_labels(y_test, y_pred, base_dir, folder_name,  filename):
    import pickle
    import pandas as pd
    df = pd.DataFrame(y_pred, index = y_test.index)
    with open(base_dir + folder_name+ filename + '.pickle', 'wb') as f:
        pickle.dump(df, f)


