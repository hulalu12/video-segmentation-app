# video-segmentation-app
This tool can remove the background surrounding a person. This functionality can be utilized to develop an application or software that removes backgrounds.


## Overview
We propose a novel end-to-end structure-aware flow generation framework for human body reshaping(FBBR), which can achieve favorable and controllable results for high-resolution images efficiently. The BR-5K is the first large-scale dataset for body reshaping, it consists of 5,000 high-quality individual portrait photos at 2K resolution collected from [Unsplash](https://unsplash.com/).

<img src="gif/438.gif" height="300px"/> <img src="gif/285.gif" height="300px"/> <img src="gif/998.gif" height="300px"/>



## BR5K Dataset
Considering that the misuse of the dataset may lead to ethical concerns, as recommended by AC, we will review the application to access the datasets. To be able to download the BR5K database, please download, sign the [agreement form](https://raw.githubusercontent.com/JianqiangRen/FlowBasedBodyReshaping/main/EULA/EULA0310.pdf), and then use your work e-mail(e.g., xx@xx.edu.cn,  xx@your_company.com) to send the form to ([jianqiang.rjq@alibaba-inc.com](jianqiang.rjq@alibaba-inc.com)).

## Getting Started
### Install Requriements
* Python >= 3.6
* torch  >= 1.2.0
* numba

### Models
* Download the pose estimator model `body_pose_model.pth` from [here](https://github.com/Hzzone/pytorch-openpose).
* Download the reshaping model body_reshape_model.pth from [google drive](https://drive.google.com/file/d/1E2kwYVCopNzcmi2U2vWXORyiJmExcezD/view?usp=sharing) or [百度网盘](https://pan.baidu.com/s/1hxlh5jipyaEi1R6NLm8KFg?pwd=17e6) (key:17e6).
* Put body_pose_model.pth and body_reshape_model.pth into the `models` folder.


### Run the Demo


    python test.py --config config/test_demo_setting.toml

 the results will be in the test_cases_output directory.

### Quantitative Evaluaton

In this repository, we take a new pretrained model of [openpose](https://github.com/Hzzone/pytorch-openpose) and achieve better quantitative performance than reported in our paper.

| Method          | SSIM  | PSNR  |LPIPS  |
|-----------------| ----  |----  |----  |
| Baseline        | 0.8339 |  24.4916 | 0.0823 |
| Paper           | 0.8354  |24.7924|0.0777 |
| This Repository | 0.8394|25.5801|0.0684|



## Citation
If our work is useful for your research, please consider citing:


	@inproceedings{ren2022structure,
	title={Structure-Aware Flow Generation for Human Body Reshaping},
	author={Ren, Jianqiang and Yao, Yuan and Lei, Biwen and Cui, Miaomiao and Xie, Xuansong},
	booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
	pages={7754--7763},
	year={2022}
	}

## Acknowledgement
We express gratitudes to [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 
and [pytorch-openpose](https://github.com/Hzzone/pytorch-openpose), as we benefit a lot from both their papers and codes.

## License
© Alibaba, 2022. For academic and non-commercial use only.
 

