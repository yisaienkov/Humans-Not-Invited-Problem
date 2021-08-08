# Humans-Not-Invited-Problem

There is solution for the [humansnotinvited problem](http://www.humansnotinvited.com/)


### Run Data Collection Process

The idea is that we run the parsing many times and count how many each picture (by its hash) was found in each of the tags (man, woman, ...). Further, for each picture, by its hash, we select the category in which it was most often encountered.

```bash
(venv) $ python main_collect_data.py

2021-08-08 16:14:23 ~ humans_not_invited_problem.collectors ~ INFO ~ iteration: 1/100; batch time: 4.66s; total time: 4.66s
...
2021-08-08 16:24:31 ~ humans_not_invited_problem.collectors ~ INFO ~ iteration: 100/100; batch time: 4.00s; total time: 613.00s
```

###

```bash
(venv) $ python main_inference.py
Input content of the html page (finish you input with 'END'):
<div class="captcha-container">
<div class="header">
<p>Select all squares with <strong>kids</strong></p>
<input type="hidden" value="kids" name="category">
</div>
<div class="content" style="width: 520.452px;">
<div class="captcha-image" data-token="$1$L911RS3.$U6HoAyuO/nhgKGb3Z.Uzv1" data-id="4" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$L911RS3.$U6HoAyuO/nhgKGb3Z.Uzv1&amp;id=4" alt=""></div><div class="captcha-image" data-token="$1$q8Z/VsjC$IWQcPqLtdnwa64Hahhpdn0" data-id="6" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$q8Z/VsjC$IWQcPqLtdnwa64Hahhpdn0&amp;id=6" alt=""></div><div class="captcha-image" data-token="$1$aYeE7j5F$g29RqMIfT7L7oijVFSy.q/" data-id="3" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$aYeE7j5F$g29RqMIfT7L7oijVFSy.q/&amp;id=3" alt=""></div><div class="captcha-image" data-token="$1$xbbReufO$51d85vtai40jXKdbXQzOT0" data-id="7" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$xbbReufO$51d85vtai40jXKdbXQzOT0&amp;id=7" alt=""></div><div class="captcha-image" data-token="$1$Xd52YQ7O$sLy.amKAOXy/HS1ylYpPb0" data-id="2" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$Xd52YQ7O$sLy.amKAOXy/HS1ylYpPb0&amp;id=2" alt=""></div><div class="captcha-image" data-token="$1$f39Na6SR$Urj410gyS6nlbEVFh0j4R1" data-id="8" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$f39Na6SR$Urj410gyS6nlbEVFh0j4R1&amp;id=8" alt=""></div><div class="captcha-image" data-token="$1$Y9x/IVx0$Vq6EGbXu5.sVAiuCxCcTU." data-id="3" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$Y9x/IVx0$Vq6EGbXu5.sVAiuCxCcTU.&amp;id=3" alt=""></div><div class="captcha-image" data-token="$1$AasgpxSR$6Kq9HrvzRzKoqQ7MmB5aA0" data-id="6" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$AasgpxSR$6Kq9HrvzRzKoqQ7MmB5aA0&amp;id=6" alt=""></div><div class="captcha-image" data-token="$1$jMUSFla8$WBzEAAyxeCr.2V7HG.R5X0" data-id="3" style="width: 169.484px;"><img src="captcha/image.php?image_name=$1$jMUSFla8$WBzEAAyxeCr.2V7HG.R5X0&amp;id=3" alt=""></div>          </div>
</div>
END
Processing...
GRID:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
SELECT NEXT IMAGES:
1
3
```