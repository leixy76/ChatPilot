# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys
import unittest

sys.path.append('..')
from chatpilot.agentica_agent import AgenticaAgent


class DeepseekTestCase(unittest.TestCase):
    def test_tool_usage(self):
        """
        usage for chat
        from openai import OpenAI
        # for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
        client = OpenAI(api_key="<your API key>", base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "Hello"},
          ],
            max_tokens=1024,
            temperature=0.7,
            stream=False
        )

        print(response.choices[0].message.content)

        """
        m = AgenticaAgent(
            model_type='deepseek', model_name="deepseek-coder", enable_search_tool=True,
            enable_url_crawler_tool=True, enable_run_python_code_tool=True, verbose=True,
            add_chat_history_to_messages=False
        )
        print(m)
        print(m.run('一句话介绍南京'))
        i = "俄乌战争的最新进展?"
        print(i)
        r = m.stream_run(i)
        print(r)
        print("===")

        print(m.run("计算88888*4444.3=?"))
        print(m.run("我前面问了啥"))


if __name__ == '__main__':
    unittest.main()
