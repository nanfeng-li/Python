'''
切换iframe
switch_to.frame方法切换，此处有id属性，可以直接用id定位切换
driver.switch_to.frame()
没有id属性和name属性为空的情况，这时候就需要先定位iframe
a = driver.find_elements_by_tag_name('iframe')[2]
driver.switch_to.frame(a)
退出框架
driver.switch_to_default_content()

contains  包含
//a[contains(@href, 'logout')]
//*[contains(text(), '退出')]
starts-with  以--开始
// a[starts-with(@class , 'a')]     @后面的class可以替换成元素的任意其他属性.
ends-with
//*[ends-with(@id,'_userName')]
'''