from src.inference.gemini import ChatGemini
from src.agent.computer import ComputerAgent
from dotenv import load_dotenv
import os
import sys

def read_prompt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: プロンプトファイル '{file_path}' が見つかりません。")
        sys.exit(1)
    except Exception as e:
        print(f"Error: ファイルの読み込み中にエラーが発生しました: {e}")
        sys.exit(1)

def main():
    load_dotenv()
    google_api_key = os.getenv('GOOGLE_API_KEY')

    llm = ChatGemini(model='gemini-2.0-flash', api_key=google_api_key, temperature=0)
    agent = ComputerAgent(llm=llm, use_vision=False, verbose=True, max_iteration=20)

    # コマンドライン引数の確認
    if len(sys.argv) > 1:
        prompt_file = sys.argv[1]
        print(f"プロンプトファイル '{prompt_file}' を読み込みます...")
        user_query = read_prompt_file(prompt_file)
        print(f"プロンプト: {user_query}")
    else:
        # 対話モード
        user_query = input('Enter your query: ')

    agent_response = agent.invoke(user_query)
    print(agent_response)

if __name__ == "__main__":
    main()