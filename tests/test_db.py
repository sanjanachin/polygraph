from flask import Flask
from flask_pymongo import pymongo
import pytest
import sys
sys.path.append("..")
import db


def test_add_delete_user():
    assert db.add_user("test_add_user")
    assert not db.add_user("test_add_user")
    assert db.delete_user("test_add_user")
    assert not db.delete_user("test_add_user")


def test_add_get_user_history():
    assert db.add_user("test_user_history")
    db.add_user_history("test_user_history", "test query", "test result")
    result = db.get_user_history("test_user_history")
    assert result[0][0] == "test query"
    assert result[0][1] == "test result"
    assert db.delete_user("test_user_history")

    assert not db.add_user_history("test_user_history_bad", "test", "test")
    assert not db.get_user_history("test_user_history_bad")
    

long_test_string = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas 
    vel auctor urna, a molestie ante. Nulla facilisi. Vivamus molestie 
    iaculis dui. Duis fringilla tincidunt ipsum in maximus. Etiam id 
    fermentum urna. Nam pulvinar sollicitudin magna, nec sollicitudin 
    ligula dictum et. Lorem ipsum dolor sit amet, consectetur adipiscing 
    elit. Integer ligula tellus, ornare eget ex eu, faucibus accumsan urna. 
    Phasellus lacinia facilisis dui, vitae gravida turpis. Etiam pharetra 
    vestibulum diam, a vestibulum orci congue eu. Curabitur nec enim 
    sapien. Vivamus porta, urna vitae semper mollis, augue eros feugiat 
    nulla, ac rhoncus libero lacus at lectus. Proin mattis sodales velit,
    ut laoreet quam molestie nec. Aenean non blandit velit. Pellentesque
    nec augue eu velit interdum efficitur sed nec turpis.
    Mauris id tempor est, eget molestie massa. Pellentesque consequat laoreet
     sapien ac efficitur. Nam eget tortor at massa dapibus vestibulum. Phasellus
      porta sed arcu ut pulvinar. Donec porttitor nisl eu nunc egestas, 
      vel tempus dolor imperdiet. Curabitur ac erat feugiat, mattis justo
       eget, accumsan nunc. Nulla mauris tellus, volutpat eget sapien a,
        tempor sollicitudin quam. Nam accumsan augue sit amet gravida 
        accumsan. Proin gravida quam lacus, in tincidunt dolor porta vel.
         Pellentesque euismod lobortis dui tempor convallis. Ut nec 
         tincidunt libero, id facilisis libero. Praesent in leo auctor,
          tempor arcu id, fermentum mi. Sed pellentesque volutpat eros
           eget semper. Ut lobortis ipsum libero, et pellentesque nunc
            bibendum et. Integer pharetra libero vehicula, sodales nisi sed, facilisis lectus.
    Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
     inceptos himenaeos. Sed nec porttitor elit. Quisque a dolor libero. 
     Ut non vulputate sapien. Fusce dolor enim, ultrices at velit ac, 
     bibendum ultricies felis. Aliquam erat volutpat. Proin convallis, 
     sem vitae aliquet pellentesque, leo arcu fermentum turpis, eget 
     semper erat nunc et dui. Nulla tortor urna, porta non sem sed, 
     vestibulum porta sapien. Pellentesque vitae facilisis quam. Nam 
     maximus urna at arcu venenatis dapibus. Proin sit amet mauris lorem. 
     Aliquam dapibus diam mi, eget elementum ligula facilisis ut. 
     Cras elit ligula, feugiat sit amet egestas imperdiet, mollis ut justo.
      Vivamus condimentum neque non congue condimentum. Vestibulum vel diam
       ac quam rutrum tristique.
    Vivamus porta quis lorem eget aliquam. Curabitur felis orci, hendrerit
     non dolor eu, malesuada porttitor neque. Nam magna enim, euismod eget
      ipsum id, dictum facilisis magna. Fusce faucibus dapibus libero ac
       luctus. Sed facilisis hendrerit massa non tincidunt. Curabitur 
       tristique felis non tortor consectetur, et euismod nibh consequat. 
       Nulla pharetra mauris arcu, non varius est finibus non. Quisque 
       faucibus sapien risus. Nam tincidunt mi a dolor dignissim, in 
       dictum libero auctor. Donec nunc leo, viverra et nisl eu, 
       efficitur hendrerit quam. Nulla convallis eleifend fermentum.
        Praesent tincidunt luctus risus a malesuada.
    Aliquam erat volutpat. Duis eros nisl, sollicitudin id porta quis,
     fringilla tempus odio. Nulla luctus venenatis iaculis. Ut tincidunt
      sagittis enim, eu ultrices turpis tincidunt et. In cursus neque 
      turpis, sit amet gravida dui lacinia non. Integer vitae lacinia metus.
       Duis tincidunt gravida semper.
    Sed sit amet neque eu libero tristique sollicitudin. In efficitur arcu 
    libero, a venenatis risus convallis consequat. Pellentesque maximus quam
     sit amet purus gravida, vel dapibus nibh dignissim. Quisque posuere diam
      et nisi iaculis, vel semper metus accumsan. Suspendisse sollicitudin non 
      risus sed rutrum. Ut mattis, leo vel facilisis efficitur, orci quam rutrum
       sem, ut fringilla ante diam eu libero. Duis feugiat risus nec leo congue
        efficitur. Donec venenatis semper magna, fringilla sollicitudin turpis.
         Aenean semper ante in orci iaculis ultricies. Vestibulum sit amet aliquam
          quam. Sed rutrum, diam et pellentesque aliquam, augue felis pellentesque
           est, a pulvinar metus lorem placerat elit. Mauris dui.
    '''


def test_add_user_history_long():
    assert db.add_user("test_user_long")
    db.add_user_history("test_user_long", long_test_string, long_test_string)
    result = db.get_user_history("test_user_long")
    assert result[0][0] == long_test_string
    assert result[0][1] == long_test_string
    db.delete_user("test_user_long")