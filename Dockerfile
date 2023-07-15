# anacondaをベースイメージ
FROM continuumio/anaconda3:2023.03-1

WORKDIR /work

EXPOSE 8888

# JupiterLabの実行
CMD [ "jupyter-lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser", "--LabApp.token=''", "--notebook-dir=/work"]