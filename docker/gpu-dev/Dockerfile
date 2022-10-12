FROM gcr.io/deeplearning-platform-release/pytorch-gpu:latest

SHELL ["/bin/bash", "-c"]

RUN apt-get update

RUN apt install libgl1-mesa-glx -y
RUN apt install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y
RUN apt install micro bat git tmux fish curl -y


RUN mkdir -p /root/.config/fish/
RUN touch /root/.config/fish/config.fish
RUN echo "starship init fish | source" >> ~/.config/fish/config.fish
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc


RUN conda init bash
RUN conda create -n mlproject python=3.10 -y
RUN echo "conda activate mlproject" >> ~/.bashrc

RUN git clone https://github.com/BayesWatch/MLProjectTemplate2022.git

SHELL ["conda", "run", "-n", "mlproject", "/bin/bash", "-c"]

RUN conda install starship
RUN starship init fish | source

RUN cd MLProjectTemplate2022 \
    && conda install -c conda-forge mamba -y \
    && mamba install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge \
    && bash install_dependencies.sh


ENTRYPOINT ["bin/bash"]