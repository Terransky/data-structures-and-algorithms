import pytest
from python.code_challenges.cc12.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    dog2 = Cat()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.enqueue(dog2)  # added a 3rd node to verify relinking correctly
    shelter.dequeue("dog")
    shelter.dequeue("dog")  # won't affect original test
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual
