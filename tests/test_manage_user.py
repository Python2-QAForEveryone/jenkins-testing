import pytest

from config.TestData import TestData as TD
from pages.LoginPage import LoginPage
from pages.ManageUserPage import ManageUserPage
from pages.NewItemPage import NewItemPageLocators
from pages.PeoplePage import PeoplePage, URLLocators, PeoplePageLocator
from pages.ProjectPage import ProjectPageLocators, ProjectPage
from pages.BuildHistoryPage import BuildHistoryPage


@pytest.mark.webtest
class TestManageUserPage:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_create_user_valid_credential(self):
        """
        TC_JN_35
        create user with valid credentials
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD)

        assert driver.get_current_url() == ManageUserPage.URL_USER_MANAGE
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_added_new_user_on_the_people_page(self):
        """
        TC_JN_37
        verify that on the PeoplePage new record in the list
        :return:
        """
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        lst = driver.get_elements_text(ManageUserPage.PEOPLE_LIST)

        assert lst[1] == ManageUserPage.USER_NAME
        lst.clear()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_check_log_in_new_user(self):
        """
        TC_JN_36
        verify that we can login with login/password new user
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver = LoginPage(self.driver)
        driver.login_jenkins(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD)

        assert driver.get_current_url() == TD.BASE_URL

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_run_the_build_job_started(self):
        """
        TC_JN_98
        verify that the job was started
        :return:
        """

        name = ProjectPage.create_new_default_job(self, ManageUserPage.CREATE_USER_JOB,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB = TD.BASE_URL + f'job/{name}/'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB)
        lst_job_before = driver.get_elements(ProjectPageLocators.COUNT_OF_BUILD_HISTORY)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_JOBS)
        lst_job_after = driver.get_elements(ProjectPageLocators.COUNT_OF_BUILD_HISTORY)

        assert len(lst_job_before) != len(lst_job_after)
        ProjectPage.delete_job(self, name)

    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_the_build_job_was_run(self):
        """
        TC_JN_99
        verify that the job was run
        :return:
        """
        name = ProjectPage.create_new_default_job(self, ManageUserPage.CREATE_USER_JOB,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB = TD.BASE_URL + f'job/{name}/'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_JOBS)
        driver = BuildHistoryPage(self.driver)
        driver.go_to_page(BuildHistoryPage.URL_BUILD_HISTORY)
        lst = driver.get_list_builded_jobs(name)

        assert len(lst) != 0
        ProjectPage.delete_job(self, name)

    @pytest.mark.regression
    def test_verify_job_in_the_list(self):
        """
        TC_JN_100
        verify that job in the list of
        :return:
        """

        name = ProjectPage.create_new_default_job(self, ManageUserPage.CREATE_USER_JOB,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB = TD.BASE_URL + f'job/{name}/'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_JOBS)
        text_num_of_job = driver.get_elements_text(ProjectPageLocators.BUILD_LAST_JOB_BY_TEXT)

        driver = PeoplePage(self.driver)
        driver.go_to_page(ManageUserPage.URL_JOB_VIEW_FROM_USER)
        text_names_of_builds = driver.get_elements_text(PeoplePageLocator.TABLE_NAMES_OF_BUILD)

        assert text_num_of_job[0] in text_names_of_builds
        ProjectPage.delete_job(self, name)

    @pytest.mark.regression
    def test_job_was_started_by_user(self):
        """
        TC_JN_101
        Verify that job was build with new Username
        :return:
        """
        name = ProjectPage.create_new_default_job(self, ManageUserPage.CREATE_USER_JOB,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB = TD.BASE_URL + f'job/{name}/'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_JOBS)
        driver.click(ProjectPageLocators.BUILD_SUCCESS_LAST_JOB)

        assert driver.get_element_text(ManageUserPage.STARTED_BY_USER) == ManageUserPage.USER_FULLNAME
        ProjectPage.delete_job(self, name)

    @pytest.mark.regression
    def test_review_all_build_ran(self):
        """
        TC_JN_102
        Verify that user has jobs ran which were early
        :return:
        """
        name = ProjectPage.create_new_default_job(self, ManageUserPage.CREATE_USER_JOB,
                                                  NewItemPageLocators.FREESTYLE_PROJECT)
        URL_JOB = TD.BASE_URL + f'job/{name}/'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB)
        driver.click(ProjectPageLocators.BUILD_NOW)
        driver.get_wait(ProjectPageLocators.BUILD_SUCCESS_JOBS)

        driver = PeoplePage(self.driver)
        driver.go_to_page(ManageUserPage.URL_JOB_VIEW_FROM_USER)
        attr_alt_of_builds = driver.get_elements_attribute(PeoplePageLocator.TABLE_STATUS_OF_BUILD, "alt")

        for alt in attr_alt_of_builds:
            assert alt == "Success"
        ProjectPage.delete_job(self, name)

    def test_delete_new_user(self):
        """
        TC_JN_38
        verify, that user present on the page
        verify, that user was deleted
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver = LoginPage(self.driver)
        driver.login_with_default_credential()
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        assert driver.is_element_present(ManageUserPage.USER_ID)

        driver.click(ManageUserPage.USER_ID_DELETE)
        driver.click(ManageUserPage.USER_ID_YES)

        assert driver.is_element_not_present(ManageUserPage.USER_ID)

    def test_deleted_new_user_on_the_people_page(self):
        """
        TC_JN_40
        verify that on the PeoplePage new record is not in the list
        :return:
        """
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        lst = driver.get_element_from_people_page(ManageUserPage.PEOPLE_LIST_ALL_RECORD)
        assert ManageUserPage.USER_NAME is not lst
        lst.clear()

    def test_verify_cant_log_in_new_user_after_deleted(self):
        """
        TC_JN_39
        verify that we can't login with deleted login/password new user
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver = LoginPage(self.driver)
        driver.login_jenkins(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD)

        assert driver.get_current_url() == LoginPage.URL_LOGIN_ERROR
        assert driver.get_element_text(LoginPage.ALERT_INVALID_DATA) == LoginPage.ALERT_TEXT

    def test_edit_new_user_fullname(self):
        """
        TC_JN_41
        verify that we can change fullname
        :return:
        """
        driver = LoginPage(self.driver)
        driver.login_with_default_credential()
        self.test_create_user_valid_credential()

        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        lst = driver.get_element_from_people_page(ManageUserPage.PEOPLE_LIST)
        assert lst[1] == ManageUserPage.USER_NAME
        assert lst[2] == ManageUserPage.USER_FULLNAME
        lst.clear()

        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.CONFIGURE_USER)

        driver.clear(ManageUserPage.INPUT_FULLNAME)
        driver.do_send_keys(ManageUserPage.INPUT_FULLNAME, ManageUserPage.USER_FULLNAME_EDIT)
        driver.clear(ManageUserPage.INPUT_EMAIL)
        driver.do_send_keys(ManageUserPage.INPUT_EMAIL, ManageUserPage.USER_EMAIL_EDIT)
        driver.clear(ManageUserPage.INPUT_PASSWORD)
        driver.do_send_keys(ManageUserPage.INPUT_PASSWORD, ManageUserPage.PASSWORD_EDIT)
        driver.clear(ManageUserPage.INPUT_CONFIRM_PASSWORD)
        driver.do_send_keys(ManageUserPage.INPUT_CONFIRM_PASSWORD, ManageUserPage.PASSWORD_EDIT)

        driver.click(ManageUserPage.USER_ID_YES)
        driver.get_element(ManageUserPage.SAVE_BUTTON).click()

        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        lst = driver.get_element_from_people_page(ManageUserPage.PEOPLE_LIST)
        assert lst[1] == ManageUserPage.USER_NAME
        assert lst[2] == ManageUserPage.USER_FULLNAME_EDIT
        lst.clear()

    def test_login_after_update(self):
        """
        TC_JN_42
        verify that we can login with login/password after updated data
        :return:
        """

        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver = LoginPage(self.driver)
        driver.login_jenkins(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD_EDIT)

        assert driver.get_current_url() == TD.BASE_URL

        self.test_delete_new_user()

    @pytest.mark.positive
    def test_create_user_with_underscore_name(self):
        """
        TC_JN_64
        create user with '_' name
        verify, that user present on the page
        :return:
        """

        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME_UNDERSCORE, ManageUserPage.PASSWORD)

        assert driver.get_elements_text(ManageUserPage.USER_ID_UNDERSCORE)[0] == ManageUserPage.USER_NAME_UNDERSCORE
        driver.delete_user(ManageUserPage.USER_NAME_UNDERSCORE)

    @pytest.mark.positive
    def test_create_user_with_hyphen_name(self):
        """
        TC_JN_72
        create user with '-' name
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME_HYPHEN, ManageUserPage.PASSWORD)

        assert driver.get_elements_text(ManageUserPage.USER_ID_HYPHEN)[0] == ManageUserPage.USER_NAME_HYPHEN
        driver.delete_user(ManageUserPage.USER_NAME_HYPHEN)

    @pytest.mark.positive
    def test_create_user_with_dot_fullname(self):
        """
        TC_JN_73
        create user with '.' fullname
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME_WITH_DOT,
                                                        ManageUserPage.USER_EMAIL)

        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_with_dot_password(self):
        """
        TC_JN_74
        create user with '.' password
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.USER_PASSWORD_DOT,
                                                        ManageUserPage.USER_FULLNAME,
                                                        ManageUserPage.USER_EMAIL)
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_with_etta_email(self):
        """
        TC_JN_75
        create user with "@" email
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME,
                                                        ManageUserPage.USER_EMAIL_ETTA)
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_with_only_dot_fullname(self):
        """
        TC_JN_76
        create user with only '.' in fullname
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME_DOT,
                                                        ManageUserPage.USER_EMAIL)
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_without_dot_email(self):
        """
        TC_JN_77
        create user without '.' email
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME,
                                                        ManageUserPage.USER_EMAIL_WO_DOT)
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_with_long_name(self):
        """
        TC_JN_78
        create user with name more than 255 ch
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME_MORE_255_SYMBOLS,
                                             ManageUserPage.PASSWORD)

        assert driver.get_elements_text(ManageUserPage.USER_ID_MORE_255_SYMBOLS)[0] \
               == ManageUserPage.USER_NAME_MORE_255_SYMBOLS
        driver.delete_user(ManageUserPage.USER_NAME_MORE_255_SYMBOLS)

    @pytest.mark.positive
    def test_create_user_with_long_password(self):
        """
        TC_JN_79
        create user with password more than 255 ch
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME,
                                             ManageUserPage.USER_PASSWORD_MORE_255_SYMBOLS)

        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_with_empty_fullname(self):
        """
        TC_JN_87
        create user with empty fullname
        verify, that user present on the page
        verify, that fullname equals User_Name
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.EMPTY_FIELD,
                                                        ManageUserPage.USER_EMAIL)
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        driver.click(ManageUserPage.USER_ID)
        assert driver.get_element_text(ManageUserPage.FULLNAME_TEXT) == ManageUserPage.USER_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.positive
    def test_create_user_with_all_date_early_but_username(self):
        """
        TC_JN_91
        create user with all data for record which we have early, but username is new
        verify, that both users present on the page
        verify, that in the both users fullname equals User_Name
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME,
                                             ManageUserPage.PASSWORD)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME_EDIT,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME,
                                                        ManageUserPage.USER_EMAIL)
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME
        assert driver.get_elements_text(ManageUserPage.USER_ID_EDIT)[0] == ManageUserPage.USER_NAME_EDIT
        driver.click(ManageUserPage.USER_ID)
        assert driver.get_element_text(ManageUserPage.FULLNAME_TEXT) == ManageUserPage.USER_FULLNAME
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.USER_ID_EDIT)
        assert driver.get_element_text(ManageUserPage.FULLNAME_TEXT) == ManageUserPage.USER_FULLNAME
        driver.delete_user(ManageUserPage.USER_NAME)
        driver.delete_user(ManageUserPage.USER_NAME_EDIT)

    @pytest.mark.negative
    def test_try_create_user_with_empty_fields(self):
        """
        TC_JN_80
        try create user with empty fields
        verify, that user leaves on the same page
        verify, that user watches notifications
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.EMPTY_FIELD,
                                                        ManageUserPage.EMPTY_FIELD,
                                                        ManageUserPage.EMPTY_FIELD,
                                                        ManageUserPage.EMPTY_FIELD)
        text_els = driver.get_elements_text(ManageUserPage.ERRORS)
        assert driver.get_current_url() == ManageUserPage.URL_USER_CREATE_ERROR
        for text_el in text_els:
            assert text_el in ManageUserPage.ERRORS_TEXT

    @pytest.mark.negative
    @pytest.mark.parametrize("name", ManageUserPage.USER_NOT_CORRECT_NAME)
    def test_try_create_user_with_not_correct_username(self, name):
        """
        TC_JN_81
        try create user with username included not alphabetic or digit letters
        TC_JN_82
        try create user with username included dot
        TC_JN_83
        try create user with username included special symbol
        TC_JN_84
        try create user with empty username
        TC_JN_89
        try create user with username included etta

        verify, that user leaves on the same page
        verify, that user watches notifications
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(name,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME,
                                                        ManageUserPage.USER_EMAIL)
        text_els = driver.get_elements_text(ManageUserPage.ERRORS)
        assert driver.get_current_url() == ManageUserPage.URL_USER_CREATE_ERROR
        for text_el in text_els:
            assert text_el in ManageUserPage.ERRORS_TEXT

    @pytest.mark.negative
    def test_try_create_user_with_not_correct_password(self):
        """
        TC_JN_85
        try create user with fill out all field, but password1 empty
        verify, that user leaves on the same page
        verify, that user watches notifications
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_with_all_diff_values(ManageUserPage.USER_NAME,
                                                                  ManageUserPage.EMPTY_FIELD,
                                                                  ManageUserPage.PASSWORD,
                                                                  ManageUserPage.USER_FULLNAME,
                                                                  ManageUserPage.USER_EMAIL)
        assert driver.get_current_url() == ManageUserPage.URL_USER_CREATE_ERROR
        assert driver.get_element_text(ManageUserPage.ERRORS) == ManageUserPage.ERROR_USER_PASSWORD

    @pytest.mark.negative
    @pytest.mark.parametrize("password", ManageUserPage.USER_PASSWORD_NOT_CORRECT)
    def test_try_create_user_with_not_correct_password(self, password):
        """
        TC_JN_86
        try create user with fill out all field, but password2 empty
        TC_JN_92
        try create user with fill out all field, but password1 not equals password2
        verify, that user leaves on the same page
        verify, that user watches notifications
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_with_all_diff_values(ManageUserPage.USER_NAME,
                                                                  ManageUserPage.PASSWORD,
                                                                  password,
                                                                  ManageUserPage.USER_FULLNAME,
                                                                  ManageUserPage.USER_EMAIL)
        assert driver.get_current_url() == ManageUserPage.URL_USER_CREATE_ERROR
        assert driver.get_element_text(ManageUserPage.ERRORS) == ManageUserPage.ERROR_USER_PASSWORD_DONT_MATCH

    @pytest.mark.negative
    def test_create_user_with_taken_username(self):
        """
        TC_JN_90
        create user with all data for record which we have early
        verify, that user leaves on the same page
        verify, that user watches notifications
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME,
                                             ManageUserPage.PASSWORD)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD_EDIT,
                                                        ManageUserPage.USER_FULLNAME_EDIT,
                                                        ManageUserPage.USER_EMAIL_EDIT)

        assert driver.get_current_url() == ManageUserPage.URL_USER_CREATE_ERROR
        assert driver.get_element_text(ManageUserPage.ERRORS) == ManageUserPage.ERROR_USER_TAKEN_NAME
        driver.delete_user(ManageUserPage.USER_NAME)

    @pytest.mark.negative
    @pytest.mark.parametrize("email", ManageUserPage.USER_EMAIL_NOT_CORRECT)
    def test_try_create_user_with_invalid_email(self, email):
        """
        TC_JN_93
        try create user with email don't include "@"
        TC_JN_88
        try create user with fill out all field, but email empty

        verify, that user leaves on the same page
        verify, that user watches notifications
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save_diff_value(ManageUserPage.USER_NAME,
                                                        ManageUserPage.PASSWORD,
                                                        ManageUserPage.USER_FULLNAME,
                                                        email)
        assert driver.get_current_url() == ManageUserPage.URL_USER_CREATE_ERROR
        assert driver.get_element_text(ManageUserPage.ERRORS) == ManageUserPage.ERROR_USER_EMAIL
