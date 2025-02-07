from src.data_collection import collect_data
from src.data_preparation import load_data, validate_data, prepare_data
from src.train_model import build_model, train_model, evaluate_model

def main():
    print('Starting data collection...')
    collect_data()

    print('Loading data...')
    data = load_data('data/processed/match_data.csv')

    print('Validating data...')
    validated_data = validate_data(data)

    print('Preparing data...')
    X_train, X_test, y_train, y_test = prepare_data(validated_data)

    print('Building model...')
    model = build_model(input_shape=X_train.shape[1])

    print('Training model...')
    train_model(model, X_train, y_train)

    print('Evaluating model...')
    evaluate_model(model, X_test, y_test)

if __name__ == '__main__':
    main()

