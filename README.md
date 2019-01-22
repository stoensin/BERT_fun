By LongGang Pang, from UC Berkeley

BERT应用之《红楼梦》对话人物提取

这个目录包含用于提取对话人物语境的脚本 conversation_extraction.ipynb，
辅助打标签的脚本 label_data_by_click_buttons.ipynb，
提取出的语境文件：honglou.py 
打过标签的训练数据：label_honglou.txt
从打过标签的数据合成百万级别新数据的脚本：augment_data.py
将训练数据转换为BERT/SQUAD可读的脚本：prepare_squad_data.py
以及预测结果文件：
res.txt (使用36000组数据训练后的预测结果）；
res_1p2million.txt（使用120万组数据训练后的预测结果）。
对比之后发现使用更多的数据训练所提升的效果有限，比较大的提升是后者在没有答案时，输出是输入的完整拷贝。


1. conversation_extraction.ipynb is used to extract conversation and the context which contains the information of the speaker.

2. honglou.py stores the extracted conversation and context information

3. label_data_by_click_buttons.ipynb is used to extract speakers by converting the context sentence to a large group of buttons.
It is much easier to click on the start and end words of the speaker (which are buttons now) to label the data.
Program will count the position automatically.

4. label_honglou.txt: the labeled speaker and contexted information for about 1562 examples

5. augment_data.py: using data augmentation to construct 1562*1562 examples by combine replacing the original speaker with speakers in different context.

6. dataset.py: use augment_data.py to create training dataset.

7. prepare_squad_data.py: convert the training dataset to json format which can be understood by BERT/SQUAD

8. prediction_results_utf8.py: the prediction results for all the context extracted from hong lou meng.

9. compare_res.py: put the context and prediction results side-by-side for a clearer comparison

10. res.txt and res_1p2million.txt: prediction results using 36000 and 1.2 million training examples correspondingly.
